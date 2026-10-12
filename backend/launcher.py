# backend/launcher.py
import subprocess, threading, os, signal, sys, logging
from pathlib import Path
from utils import VENV_PY, CLASSIFIER_SCRIPT, CLASSIFIER_DIR

TIMEOUT = 120   # seconds 


def _kill(proc: subprocess.Popen) -> None:
    """Terminate process (and, on Windows, its children) after TIMEOUT."""
    try:
        if sys.platform == "win32":
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(proc.pid)],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        else:
            os.killpg(os.getpgid(proc.pid), signal.SIGTERM)
    except Exception as e:
        logging.warning("while killing classifier: %s", e)


def launch_classifier(activity: str, timeout: int = TIMEOUT) -> None:
    """
    Spawn classifier1.py in its virtual-env Python, passing <activity> so the
    script can load rfc_<activity>_model2.pkl.  Output is streamed into the
    server log.  The process is auto-killed after TIMEOUT seconds.
    """
    cmd = [str(VENV_PY), "-u", str(CLASSIFIER_SCRIPT), activity]

    logging.info("Launching classifier: %s", " ".join(cmd))

    def _run() -> None:
        logging.info("[launcher] VENV_PY          → %s", VENV_PY)
        logging.info("[launcher] CLASSIFIER_SCRIPT → %s", CLASSIFIER_SCRIPT)
        proc = subprocess.Popen(
            cmd,
            cwd=CLASSIFIER_DIR,                 
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            preexec_fn=None if sys.platform == "win32" else os.setsid,
        )

        timer = threading.Timer(timeout, _kill, args=(proc,))
        timer.start()

        for line in proc.stdout:
            print("[classifier]", line.rstrip())


        proc.wait()
        timer.cancel()
        logging.info("Classifier exited with %s", proc.returncode)

    threading.Thread(target=_run, daemon=True).start()
    print("Classifier script started")
