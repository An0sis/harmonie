function openModal(imageUrl) {
    // Get the modal and the modal image
    let modal = document.getElementById('modal');
    let modalImg = document.getElementById('modal-img');

    // Set the source of the modal image to the provided URL
    modalImg.src = imageUrl;

    // Display the modal
    modal.style.display = 'flex';

    // Add a click event listener to the modal to hide it when clicked
    modal.addEventListener('click', function() {
        modal.style.display = 'none';
    });
}