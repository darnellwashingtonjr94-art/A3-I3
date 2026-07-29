document.addEventListener('DOMContentLoaded', () => {
    const triggerBtn = document.getElementById('trigger-api-btn');
    const consoleOutput = document.getElementById('console-output');

    triggerBtn.addEventListener('click', async () => {
        consoleOutput.textContent = "Executing request to /api...";
        triggerBtn.disabled = true;
        
        try {
            // Vercel routes /api automatically to the python serverless function
            const response = await fetch('/api');
            if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
            
            const data = await response.json();
            consoleOutput.textContent = JSON.stringify(data, null, 2);
        } catch (error) {
            consoleOutput.textContent = `Execution failed:\n${error.message}`;
        } finally {
            triggerBtn.disabled = false;
        }
    });
});
