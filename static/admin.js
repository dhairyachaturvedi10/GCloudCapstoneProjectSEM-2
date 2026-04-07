let allRegistrations = []; // Master list to hold our data

// 1. Fetch data from Python when the page loads
function loadData() {
    fetch('/api/registrations')
        .then(response => response.json())
        .then(data => {
            allRegistrations = data;
            renderTable(allRegistrations); // Draw the table
        });
}

// 2. Draw the table rows based on the provided data
function renderTable(dataToRender) {
    const tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = ''; // Clear the table first

    dataToRender.forEach(student => {
        const row = document.createElement('tr');
        
        row.innerHTML = `
            <td>${student.id}</td>
            <td>${student.fullName}</td>
            <td>${student.collegeId}</td>
            <td>${student.eventName}</td>
            <td>
                <button class="delete-btn" onclick="deleteRecord(${student.id})">DELETE</button>
            </td>
        `;
        tableBody.appendChild(row);
    });
}

// 3. The Real-Time Search Filter
document.getElementById('searchInput').addEventListener('input', function(e) {
    const searchTerm = e.target.value.toLowerCase();
    
    // Filter the master list
    const filteredData = allRegistrations.filter(student => 
        student.fullName.toLowerCase().includes(searchTerm) || 
        student.collegeId.toLowerCase().includes(searchTerm) ||
        student.eventName.toLowerCase().includes(searchTerm)
    );
    
    // Redraw the table with only the matching results
    renderTable(filteredData);
});

// 4. The Delete Function
function deleteRecord(id) {
    // Add a safety confirmation popup
    if (confirm("WARNING: Are you sure you want to delete this registration?")) {
        
        fetch(`/api/registrations/${id}`, { 
            method: 'DELETE' 
        })
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                loadData(); // Reload the data from the server to refresh the table
            }
        });
    }
}

// Start the whole process
loadData();