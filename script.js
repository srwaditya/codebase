// Initialize AOS (Animate On Scroll)
document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,
        once: true,
        offset: 100
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('nav a').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            targetSection.scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

    // Animate skill bars on scroll
    const skillLevels = document.querySelectorAll('.skill-level');
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.width = entry.target.style.width;
            }
        });
    });

    skillLevels.forEach(skillLevel => {
        observer.observe(skillLevel);
    });
});

// Function to download resume PDF
function downloadResume() {
    // Create a link element
    const link = document.createElement('a');
    
    // Set the link's href to your PDF file
    // Replace this URL with the actual path to your PDF resume
    link.href = 'Aditya_Kumar_Resume.pdf';
    
    // Set the download attribute with the desired file name
    link.download = 'Aditya_Kumar_Resume.pdf';
    
    // Append link to body
    document.body.appendChild(link);
    
    // Trigger the download
    link.click();
    
    // Remove the link from the document
    document.body.removeChild(link);
}
