<script>
    // Function to update the main product image
    function updateMainImage(imageUrl) {
        document.getElementById('mainImage').src = imageUrl;
    }

    // Function to navigate through gallery images using arrow keys
    document.addEventListener('keydown', function(event) {
        const galleryThumbnails = document.querySelectorAll('.gallery-thumb img');
        const currentMainImage = document.getElementById('mainImage').src;
        let currentIndex = -1;

        // Find the index of the current main image in the gallery thumbnails
        galleryThumbnails.forEach((thumbnail, index) => {
            if (thumbnail.src === currentMainImage) {
                currentIndex = index;
            }
        });

        // Handle arrow key events
        if (event.key === 'ArrowLeft') {
            if (currentIndex > 0) {
                updateMainImage(galleryThumbnails[currentIndex - 1].src);
            }
        } else if (event.key === 'ArrowRight') {
            if (currentIndex < galleryThumbnails.length - 1) {
                updateMainImage(galleryThumbnails[currentIndex + 1].src);
            }
        }
    });
</script>