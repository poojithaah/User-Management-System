// Function to fetch all users from FastAPI
// and display them in the table

async function loadUsers() {

    let response = await fetch('/all-users');

    let users = await response.json();

    let table = document.getElementById("userTable");

    let searchText =
        document.getElementById("searchInput")
        .value
        .toLowerCase();

    table.innerHTML = "";

    let count = 0;

    for(let id in users){

        let name =
            users[id].name.toLowerCase();

        if(!name.includes(searchText)){
            continue;
        }

        count++;

        table.innerHTML += `
        <tr>
            <td>${id}</td>
            <td>${users[id].name}</td>
            <td>${users[id].gender}</td>

            <td>
                <div class="action-buttons">

                    <button
                        class="edit-btn"
                        onclick="editUser(${id}, '${users[id].name}')">
                        Modify
                    </button>

                    <button
                        class="delete-btn"
                        onclick="deleteUser(${id})">
                        Delete
                    </button>

                </div>
            </td>
        </tr>
        `;
    }

    document.getElementById("userCount").innerText = count;
}

// Function to edit user name
function editUser(id, currentName){

    let newName = prompt(
        "Enter new name:",
        currentName
    );

    if(newName){

        updateUser(id, newName);

    }
    }

// Function to send updated name to backend
async function updateUser(id, newName){

    await fetch(
        `/users-update/${id}/${newName}`,
        {
            method:'PUT'
        }
    );

     // Reload table after update
    loadUsers();
    }

// Function to delete a user
async function deleteUser(id) {

    // Ask confirmation before deleting
    let confirmDelete = confirm(
        "Are you sure you want to delete this user?"
    );

    if (!confirmDelete) {
        return;
    }

    await fetch(`/users-delete/${id}`, {
        method: "DELETE"
    });

    // Reload table after deletion
    loadUsers();
}


// Function to add a new user
async function addUser(){

    let id = document.getElementById("id").value;
    let name = document.getElementById("name").value;
    let gender = document.getElementById("gender").value;

    await fetch(
        `/users-entry/${id}/${name}/${gender}`,
        {
            method:'POST'
        }
    );

    loadUsers();

    // Clear input fields after adding user
    document.getElementById("id").value = "";
    document.getElementById("name").value = "";
}

// Load users automatically when page opens
loadUsers();
