document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the assessment page
    const assessmentForm = document.getElementById('assessmentForm');
    if (assessmentForm) {
        const questions = document.querySelectorAll('.question-item');
        const totalQuestions = questions.length;
        const progressBar = document.getElementById('progressBar');
        const progressText = document.getElementById('progressText');
        
        // Function to update progress
        function updateProgress() {
            const answeredQuestions = document.querySelectorAll('input[type="radio"]:checked').length;
            const progress = (answeredQuestions / totalQuestions) * 100;
            
            progressBar.style.width = progress + '%';
            progressText.textContent = `${answeredQuestions}/${totalQuestions} questions answered`;
        }
        
        // Add event listeners to all radio buttons
        document.querySelectorAll('input[type="radio"]').forEach(function(radio) {
            radio.addEventListener('change', updateProgress);
        });
        
        // Initial progress update
        updateProgress();
    }
    
    // Check if we're on the results page
    const resultsSection = document.querySelector('.results');
    if (resultsSection) {
        // Add animation to the score bars
        const scoreFillers = document.querySelectorAll('.score-fill');
        
        // Animate score bars after a small delay
        setTimeout(function() {
            scoreFillers.forEach(function(filler) {
                filler.style.transition = 'width 1s ease-in-out';
                filler.style.width = filler.getAttribute('style').split(':')[1];
            });
        }, 300);
    }
});