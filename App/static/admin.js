function showCreateCompetition() {
    document.getElementById("content").innerHTML = `
        <h2>Create Competition</h2>
        <p>Please enter the following details to create competition:</p>
        <form id="createCompetitionForm">
            <label for="competitionName">Competition Name:</label>
            <input type="text" id="competitionName" name="competitionName" required><br>

            <label for="startDate">Start Date:</label>
            <input type="date" id="startDate" name="startDate" required><br>

            <label for="endDate">End Date:</label>
            <input type="date" id="endDate" name="endDate" required><br>

            <label for="description">Competition Description:</label>
            <textarea id="description" name="description" rows="4" required></textarea><br>

            <label for="addUsers">Add Users:</label>
            <input type="text" id="addUsers" name="addUsers" placeholder="Enter user emails" required><br>

            <button type="button" onclick="createCompetition()">Create Competition</button>
        </form>
    `;
}

function showCompetitionResults() {
    document.getElementById("content").innerHTML = `
        <h2>Competition Results</h2>
        <div>
            <label for="compName">Competition Name:</label>
            <input type="text" id="compName" name="compName" required><br>

            <label for="compID">Competition ID:</label>
            <input type="text" id="compID" name="compID" required><br>

            <label for="enterUserID">Enter User ID of Participants:</label>
            <input type="text" id="enterUserID" name="enterUserID" placeholder="Enter user IDs" required><br>

            <button type="button" onclick="enterResults()">Enter Results</button>
        </div>
    `;
}

async function editUserRankings() {
const response = await fetch('http://localhost:3000/user-rankings');
userRankings = await response.json();

// Generate HTML for editing user rankings
let html = '<h2>Edit User Rankings</h2>';
html += '<ul>';

userRankings.forEach(user => {
html += `<li>User ID: ${user.userId} - Ranking: ${user.ranking} <input type="number" min="1" max="10" value="${user.ranking}" id="user${user.userId}Ranking" /> </li>`;
});

html += '</ul>';
html += '<button onclick="saveUserRankings()">Save Rankings</button>';

document.getElementById("content").innerHTML = html;
}

async function saveUserRankings() {
const updatedRankings = userRankings.map(user => {
const inputElement = document.getElementById(`user${user.userId}Ranking`);
return { userId: user.userId, ranking: parseInt(inputElement.value) };
});

const response = await fetch('http://localhost:3000/update-rankings', {
method: 'POST',
headers: {
    'Content-Type': 'application/json',
},
body: JSON.stringify(updatedRankings),
});

const result = await response.json();
alert(result.message);
}

function editProfile() {
// Display existing user profile data
const html = `
<h2>Edit Profile</h2>
<form id="editProfileForm">
    <label for="profilePicture">Profile Picture:</label>
    <input type="file" id="profilePicture" name="profilePicture" accept="image/*"><br>

    <label for="userName">Name:</label>
    <input type="text" id="userName" name="userName" value="${userProfile.name}" required><br>

    <label for="userEmail">Email:</label>
    <input type="email" id="userEmail" name="userEmail" value="${userProfile.email}" required><br>

    <!-- Add more fields as needed -->

    <button type="button" onclick="saveProfileChanges()">Save Changes</button>
</form>
`;

document.getElementById("content").innerHTML = html;
}

function saveProfileChanges() {
// Update user profile data
userProfile.name = document.getElementById("userName").value;
userProfile.email = document.getElementById("userEmail").value;

// Handle profile picture upload
const profilePictureInput = document.getElementById("profilePicture");
if (profilePictureInput.files.length > 0) {
const newProfilePicture = profilePictureInput.files[0];
// You can handle the new profile picture, e.g., upload to server or store in local storage
// For simplicity, let's just log the file name to the console.
console.log("New Profile Picture:", newProfilePicture.name);
}

// Save updated profile to local storage or send to the server
localStorage.setItem('userProfile', JSON.stringify(userProfile));

alert('Profile changes saved successfully!');
}

function createCompetition() {
// Gather data from the form
const competitionName = document.getElementById("competitionName").value;
const startDate = document.getElementById("startDate").value;
const endDate = document.getElementById("endDate").value;
const description = document.getElementById("description").value;
const addUsers = document.getElementById("addUsers").value.split(',');

// Validate the data (you can add more validation as needed)
if (!competitionName || !startDate || !endDate || !description || addUsers.length === 0) {
alert('Please fill in all the required fields.');
return;
}
console.log('Competition Name:', competitionName);
console.log('Start Date:', startDate);
console.log('End Date:', endDate);
console.log('Description:', description);
console.log('Added Users:', addUsers);


document.getElementById("createCompetitionForm").reset();

alert('Competition created successfully!');
}

function enterResults() {
// Gather data from the form
const compName = document.getElementById("compName").value;
const compID = document.getElementById("compID").value;
const enterUserID = document.getElementById("enterUserID").value;

if (!compName || !compID || !enterUserID) {
alert('Please fill in all the required fields.');
return;
}

console.log('Competition Name:', compName);
console.log('Competition ID:', compID);
console.log('Entered User IDs:', enterUserID);

document.getElementById("competitionResultsForm").reset();

alert('Results entered successfully!');
}

function notifyUsers() {

    alert("Notifying users is not implemented yet.");
}
function createCompetition() {
const competitionName = document.getElementById("competitionName").value;
const startDate = document.getElementById("startDate").value;
const endDate = document.getElementById("endDate").value;
const description = document.getElementById("description").value;
const addUsers = document.getElementById("addUsers").value.split(',');

if (!competitionName || !startDate || !endDate || !description || addUsers.length === 0) {
alert('Please fill in all the required fields.');
return;
}

console.log('Competition Name:', competitionName);
console.log('Start Date:', startDate);
console.log('End Date:', endDate);
console.log('Description:', description);
console.log('Added Users:', addUsers);


document.getElementById("createCompetitionForm").reset();

alert('Competition created successfully!');
}