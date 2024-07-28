document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('http://127.0.0.1:8000/api/v1/upload', {
        method: 'POST',
        body: formData,
    });

    if (response.ok) {
        const result = await response.json();
        alert(result.message);
    } else {
        alert("Failed to upload the file.");
    }
});

document.getElementById('queryButton').addEventListener('click', async function () {
    const queryInput = document.getElementById('queryInput').value;
    const filename = document.getElementById('fileInput').files[0].name;

    const response = await fetch('http://127.0.0.1:8000/api/v1/analyze', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            task: 'analyze',
            query: queryInput,
            filename: filename,
        }),
    });

    if (response.ok) {
        const result = await response.json();
        document.getElementById('responseOutput').textContent = JSON.stringify(result, null, 2);
    } else {
        alert("Failed to process the query.");
    }
});


