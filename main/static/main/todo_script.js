

window.onload = () => {
    const el = document.getElementById('todo_button')
    if (el){
        el.addEventListener('click', event => {
            document.getElementById('todo_form_div').append('<p> a todo </a>')
        })
    }
}