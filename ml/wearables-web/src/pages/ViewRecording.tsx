import React, { useState, useEffect } from 'react';

const ViewRecordingPage: React.FC = () => {
    const [files, setFiles] = useState<string[]>([]);
    const [selectedFile, setSelectedFile] = useState<string>('');
    const [uploadResult, setUploadResult] = useState<string>('');

    useEffect(() => {
        fetch('/api/files')
            .then(res => res.json())
            .then(setFiles)
            .catch(() => setUploadResult('❌ Failed to load files.'));
    }, []);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setUploadResult('Uploading...');

        const formData = new FormData();
        formData.append('selected_file', selectedFile);

        try {
            const res = await fetch('/api/start', {
                method: 'POST',
                body: formData,
            });

            const text = await res.text();
            setUploadResult(text);
        } catch {
            setUploadResult('❌ Error uploading data.');
        }
    };

    return (
        <div className="p-4" style={{ backgroundColor: '#2a2f37', color: '#f1f3f5' }}>
            <h1>Sensor Recordings</h1>

            <form onSubmit={handleSubmit}>
                <label htmlFor="selected_file">Select Recording:</label>
                <select
                    id="selected_file"
                    className="form-select mb-3"
                    value={selectedFile}
                    onChange={(e) => setSelectedFile(e.target.value)}
                >
                    <option value="">-- Select a file --</option>
                    {files.map(file => (
                        <option key={file} value={file}>{file}</option>
                    ))}
                </select>
                <button className="btn btn-primary" type="submit">Watch Recording</button>
            </form>


            <div className="mt-5 px-0">
                <div className="row g-3">
                    {[1, 2, 3].map(id => (
                        <div key={id} className="col-md-6">
                            <iframe
                                title={`Panel ${id}`}
                                src={`http://127.0.0.1:4000/d-solo/cel8dsmiktipsc/wearables?orgId=1&from=now-3m&to=now&timezone=browser&refresh=100ms&panelId=${id}&__feature.dashboardSceneSolo`}
                                width="100%"
                                height="380"
                                frameBorder="0"
                                style={{
                                    borderRadius: '12px',
                                    boxShadow: '0 4px 20px rgba(0, 0, 0, 0.3)',
                                    overflow: 'hidden',
                                }}
                            />

                        </div>
                    ))}
                </div>
            </div>

        </div>
    );
};

export default ViewRecordingPage;
