function chooseFileType(fileType) {
    var fileInput = document.getElementById('imageUpload');
    var submitButton = document.querySelector('input[type="submit"]');
    
    if (fileType === 'image') {
        fileInput.accept = 'image/*';
    } else if (fileType === 'pdf') {
        fileInput.accept = '.pdf';
    }

    fileInput.style.display = 'block';
    submitButton.style.display = 'block';
}

var uploadForm = document.getElementById('uploadForm');
uploadForm.addEventListener('submit', function(event) {
    event.preventDefault();
    var fileInput = document.getElementById("imageUpload");
    var file = fileInput.files[0];
    
    if (!file) {
        console.error("No file selected");
        return;
    }
    var formData = new FormData();
    formData.append("filename", file);

    fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData
    })
    .then(response => {
        if (response.ok) {
            console.log("File uploaded successfully");
            response.json().then(data => {
                // console.log(data.image_data); // Log image_data property
                console.log(data); // Log the entire response data
                document.getElementById('text').innerHTML = data.csv_file;
                var uploadedImage = document.getElementById('previewImage');
                uploadedImage.src = 'data:image/png;base64,' + data.image_data;
                uploadedImage.alt = 'Uploaded Image';
                console.log(uploadedImage)
            });
        } else {
            console.error("Error:", response.statusText);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
});

document.getElementById('imageUpload').addEventListener('change', function() {
    var file = this.files[0];
    var reader = new FileReader();

    reader.onload = function(e) {
        var previewImage = document.getElementById('previewImage');
        var previewPdf = document.getElementById('previewPdf');
        if (file.type.includes('image')) {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block';
            previewPdf.style.display = 'none';
        } else if (file.type === 'application/pdf') {
            previewPdf.src = e.target.result;
            previewPdf.style.display = 'block';
            previewImage.style.display = 'none';
        }
        document.getElementById('previewContainer').style.display = 'block';
    }

    reader.readAsDataURL(file);
});
