document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('textInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');
    const errorDiv = document.getElementById('error');

    const emotionValue = document.getElementById('emotionValue');
    const riskValue = document.getElementById('riskValue');
    const emotionConf = document.getElementById('emotionConf');
    const riskConf = document.getElementById('riskConf');

    const driftSection = document.getElementById('drift-section');
    const planTitle = document.getElementById('plan-title');
    const planType = document.getElementById('plan-type');
    const planDuration = document.getElementById('plan-duration');
    const planSteps = document.getElementById('plan-steps');

    analyzeBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) {
            alert('Please enter some text.');
            return;
        }

        // Reset UI
        resultDiv.classList.add('hidden');
        driftSection.classList.add('hidden');
        errorDiv.classList.add('hidden');
        loadingDiv.classList.remove('hidden');
        analyzeBtn.disabled = true;

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Something went wrong');
            }

            // Update UI with results
            emotionValue.textContent = data.emotion;
            riskValue.textContent = data.risk_level;

            // Update Progress Bars
            const emotionPct = (data.emotion_confidence * 100).toFixed(1);
            const riskPct = (data.risk_confidence * 100).toFixed(1);

            document.getElementById('emotionBar').style.width = `${emotionPct}%`;
            document.getElementById('riskBar').style.width = `${riskPct}%`;

            // Color coding & Emergency Widget
            const emergencyWidget = document.getElementById('emergency-widget');
            
            if (data.risk_level === 'High') {
                riskValue.style.color = 'var(--risk-high)';
                document.getElementById('riskBar').style.backgroundColor = 'var(--risk-high)';
                emergencyWidget.classList.remove('hidden');
            } else if (data.risk_level === 'Medium') {
                riskValue.style.color = 'var(--risk-medium)';
                document.getElementById('riskBar').style.backgroundColor = 'var(--risk-medium)';
                emergencyWidget.classList.add('hidden');
            } else {
                riskValue.style.color = 'var(--risk-low)';
                document.getElementById('riskBar').style.backgroundColor = 'var(--risk-low)';
                emergencyWidget.classList.add('hidden');
            }

            resultDiv.classList.remove('hidden');

            // --- DRIFT Planner Integration ---
            try {
                const planResponse = await fetch('/drift-plan', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        text: text,
                        emotion: data.emotion,
                        risk_level: data.risk_level
                    })
                });

                const planData = await planResponse.json();

                if (planResponse.ok) {
                    renderPlan(planData);
                    driftSection.classList.remove('hidden');
                }
            } catch (planError) {
                console.error("Failed to fetch plan:", planError);
            }

        } catch (error) {
            errorDiv.textContent = error.message;
            errorDiv.classList.remove('hidden');
        } finally {
            loadingDiv.classList.add('hidden');
            analyzeBtn.disabled = false;
        }
    });

    function renderPlan(plan) {
        planTitle.textContent = plan.plan_title;
        planType.textContent = plan.solution_type;
        planDuration.textContent = plan.duration;

        planSteps.innerHTML = ''; // Clear previous steps

        plan.steps.forEach((step, index) => {
            const stepDiv = document.createElement('div');
            stepDiv.className = 'timeline-step';
            stepDiv.innerHTML = `
                <div class="timeline-marker"></div>
                <div class="timeline-content">
                    <span class="day-badge">${step.day}</span>
                    <span class="focus-label">Focus: ${step.focus}</span>
                    <p class="activity-text">${step.activity}</p>
                </div>
            `;
            planSteps.appendChild(stepDiv);
        });
    }
});
