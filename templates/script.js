document.getElementById('uploadForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const fileInput = document.getElementById('fileInput');
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const response = await fetch('http://127.0.0.1:8000/api/v1/upload', {
        method: 'POST',
        body: formData,
    });

    const result = await response.json();
    alert(result.message);
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

    const result = await response.json();
    document.getElementById('responseOutput').textContent = JSON.stringify(result, null, 2);
});
