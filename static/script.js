// --- 1. COUNTDOWN TIMER LOGIC ---
const countdownEl = document.getElementById('countdown');
if (countdownEl) {
    const targetDate = new Date(countdownEl.getAttribute('data-target')).getTime();

    const timerInterval = setInterval(function() {
        const now = new Date().getTime();
        const distance = targetDate - now;

        if (distance < 0) {
            clearInterval(timerInterval);
            countdownEl.innerHTML = "EVENT HAS STARTED";
            return;
        }

        document.getElementById('days').innerText = String(Math.floor(distance / (1000 * 60 * 60 * 24))).padStart(2, '0');
        document.getElementById('hours').innerText = String(Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60))).padStart(2, '0');
        document.getElementById('mins').innerText = String(Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60))).padStart(2, '0');
        document.getElementById('secs').innerText = String(Math.floor((distance % (1000 * 60)) / 1000)).padStart(2, '0');
    }, 1000);
}

// --- 2. MODAL LOGIC (Fixed) ---
function openModal(title, date, description, imageSrc) {
    document.getElementById('modalTitle').innerText = title;
    document.getElementById('modalDate').innerText = date;
    document.getElementById('modalDesc').innerText = description;
    document.getElementById('modalImg').src = imageSrc;
    document.getElementById('modalRegisterBtn').href = "/register?event=" + encodeURIComponent(title);
    
    const modal = document.getElementById('eventModal');
    modal.style.display = 'flex'; 
    setTimeout(() => { modal.classList.add('show'); }, 10); 
    document.body.classList.add('no-scroll'); 
}

function closeModal() {
    const modal = document.getElementById('eventModal');
    modal.classList.remove('show');
    setTimeout(() => { modal.style.display = 'none'; }, 300);
    document.body.classList.remove('no-scroll');
}

// --- 3. FORM SUBMISSION LOGIC ---
const form = document.getElementById('registrationForm');
if (form) {
    form.addEventListener('submit', function(e) {
        e.preventDefault(); 

        const fullName = document.getElementById('fullName').value;
        const collegeId = document.getElementById('collegeId').value;
        const section = document.getElementById('section').value;     
        const semester = document.getElementById('semester').value;   
        
        const selectedEventRadio = document.querySelector('input[name="eventName"]:checked');
        const eventName = selectedEventRadio ? selectedEventRadio.value : null;

        if (!eventName) {
            alert("Please select an event to register.");
            return;
        }

        fetch('/api/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ fullName, collegeId, semester, section, eventName })
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                const msgDiv = document.getElementById('successMessage');
                msgDiv.innerHTML = "✓ " + data.message;
                msgDiv.classList.remove('hidden');
                form.reset(); 
            }
        })
        .catch((error) => console.error('Error:', error));
    });
}