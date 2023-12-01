function viewCompetitions() {
    let html = '<h2>Competitions</h2>';
    if (competitions.length === 0) {
        html += '<p>No competitions available.</p>';
    } else {
        html += '<ul>';
        competitions.forEach(competition => {
            html += `<li>${competition.name} - ${competition.startDate} to ${competition.endDate}</li>`;
        });
        html += '</ul>';
    }
    document.getElementById("content").innerHTML = html;
}

function viewRankings() {
    let html = '<h2>Current Rankings</h2>';
    if (rankings.length === 0) {
        html += '<p>No rankings available.</p>';
    } else {
        // Display top 3 rankings
        html += '<ol>';
        for (let i = 0; i < Math.min(3, rankings.length); i++) {
            html += `<li>${rankings[i].userName} - Ranking: ${rankings[i].ranking}</li>`;
        }
        html += '</ol>';

        // Display the rest of the rankings
        if (rankings.length > 3) {
            html += '<p>Other Participants:</p>';
            html += '<ul>';
            for (let i = 3; i < rankings.length; i++) {
                html += `<li>${rankings[i].userName} - Ranking: ${rankings[i].ranking}</li>`;
            }
            html += '</ul>';
        }
    }
    document.getElementById("content").innerHTML = html;
}

function viewRankingResults() {
    // Add logic to display ranking results based on your requirements
    alert("View Ranking Results - Not implemented yet.");
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

const profilePictureInput = document.getElementById("profilePicture");
if (profilePictureInput.files.length > 0) {
const newProfilePicture = profilePictureInput.files[0];

console.log("New Profile Picture:", newProfilePicture.name);
}

localStorage.setItem('userProfile', JSON.stringify(userProfile));

alert('Profile changes saved successfully!');
}