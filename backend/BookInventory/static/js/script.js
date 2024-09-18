document.addEventListener('DOMContentLoaded', function () {
    const addBookForm = document.getElementById('add-book-form');
    const filterForm = document.getElementById('filter-form');
    const booksList = document.getElementById('books-list');
    const exportCsvButton = document.getElementById('export-csv');

    // Add Book
    addBookForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(addBookForm);
        const data = Object.fromEntries(formData);

        fetch('http://127.0.0.1:8000/inventory/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            alert('Book added successfully');
            addBookForm.reset();
            fetchBooks(); // Refresh the list
        })
        .catch(error => console.error('Error:', error));
    });

    // Filter Books
    filterForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(filterForm);
        const queryString = new URLSearchParams(formData).toString();

        fetch(`http://127.0.0.1:8000/inventory/?${queryString}`, {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            populateBooksTable(data);
        })
        .catch(error => console.error('Error:', error));
    });

    // Export CSV
    exportCsvButton.addEventListener('click', function () {
        window.location.href = 'http://127.0.0.1:8000/inventory/export/csv/';
    });

    // Fetch and display books
    function fetchBooks() {
        fetch('http://127.0.0.1:8000/inventory/', {
            method: 'GET',
        })
        .then(response => response.json())
        .then(data => {
            populateBooksTable(data);
        })
        .catch(error => console.error('Error:', error));
    }

    function populateBooksTable(books) {
        booksList.innerHTML = `
            <table>
                <thead>
                    <tr>
                        <th>Entry ID</th>
                        <th>Title</th>
                        <th>Author</th>
                        <th>Genre</th>
                        <th>Publication Date</th>
                        <th>ISBN</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    ${books.map(book => `
                        <tr>
                            <td>${book.entry_id}</td>
                            <td>${book.title}</td>
                            <td>${book.author}</td>
                            <td>${book.genre}</td>
                            <td>${book.publication_date}</td>
                            <td>${book.isbn}</td>
                            <td>
                                <button onclick="deleteBook(${book.entry_id})">Delete</button>
                            </td>
                        </tr>
                    `).join('')}
                </tbody>
            </table>
        `;
    }

    window.deleteBook = function (id) {
        fetch(`http://127.0.0.1:8000/inventory/${id}/`, {
            method: 'DELETE',
        })
        .then(response => {
            if (response.ok) {
                alert('Book deleted successfully');
                fetchBooks(); // Refresh the list
            } else {
                return response.json().then(data => alert(data.error));
            }
        })
        .catch(error => console.error('Error:', error));
    };

    fetchBooks(); // Initial fetch
});