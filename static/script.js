function saveArticle(ind, username) {
  let title = document.getElementById(`headline${ind}`).textContent.trim()
  let url = document.getElementById(`url${ind}`).href

  if (localStorage[username] != null) {
    let prev = JSON.parse(localStorage[username])
    prev[title] = url
    localStorage[username] = JSON.stringify(prev)
  } else {
    let store = { [title]: url }
    store = JSON.stringify(store)
    localStorage[username] = store
  }
}

//Error
function delete_article(ind, username) {
  let article = document.getElementById(`article${ind}`).textContent.trim()
  let data = JSON.parse(localStorage[username])
  delete data[article]
  localStorage[username] = JSON.stringify(data)
  get_saved_articles(username)
}

function get_saved_articles(username) {
  let saved_section = document.getElementById('saved-articles')
  if (saved_section != null) {
    document.getElementById('saved-articles').innerHTML = ''
    if (localStorage[username].length > 3) {
      let articles = JSON.parse(localStorage[username])
      let count = 0
      for (article in articles) {
        saved_section.innerHTML += `<div class="list-group-item list-group-item-action d-flex justify-content-between">
        <a href=${articles[article]} class="card-link" id="article${count}">
          ${article}
        </a>
        <button class="btn btn-danger custom-delete-btn" id="del-btn${count}" onclick="delete_article(${count++}, '${username}')">
          <i class="fa fa-trash" aria-hidden="true"></i>
        </button>
      </div>`
      }
    } else {
      saved_section.innerHTML += `<p href="#" class='list-group-item list-group-item-action'>Save some articles to see them here.</p>`
    }
  }
}
