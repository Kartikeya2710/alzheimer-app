function displayImage(event) {
    const fileInput = event.target;
    const selectedImage = document.getElementById('selected-image');
    const imageContainer = document.getElementById('image-container');
    const file = fileInput.files[0];
    const reader = new FileReader();

    if (file) {
        reader.onload = function (e) {
            const selectedImageUrl = e.target.result;
            localStorage.setItem('selectedImageUrl', selectedImageUrl);
            selectedImage.src = selectedImageUrl;
            imageContainer.style.display = 'block';
        };

        reader.readAsDataURL(file);
        localStorage.removeItem('selectedImageUrl'); // Remove previous image URL
    } else {
        localStorage.removeItem('selectedImageUrl');
        selectedImage.src = '';
        imageContainer.style.display = 'none';
    }
}

function clearImage() {
    const selectedImage = document.getElementById('selected-image');
    const imageContainer = document.getElementById('image-container');
    selectedImage.src = '';
    imageContainer.style.display = 'none';
    localStorage.removeItem('selectedImageUrl');
}

window.addEventListener('load', function() {
    const selectedImageUrl = localStorage.getItem('selectedImageUrl');
    const selectedImage = document.getElementById('selected-image');
    selectedImage.src = selectedImageUrl;
    if (selectedImageUrl) {
        const imageContainer = document.getElementById('image-container');
        imageContainer.style.display = 'block';
    }
});