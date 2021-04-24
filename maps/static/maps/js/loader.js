function loadAll(container, csrf, url)
{
    var formData = new FormData();
    formData.append(csrf.name, csrf.value); //csrf token
    fetch(url, {
        method: 'POST',
        body: formData
    }).then(res => res.json()).then(res => {
        if(res.route_status == 'loaded')
        {
            container.innerHTML = '';
            
            res.routes.forEach((route) => {
                var itemDiv = document.createElement('div');
                itemDiv.setAttribute('class', 'd-flex list-group-item');
                container.appendChild(itemDiv);
                var nameSpan = document.createElement('span');
                nameSpan.setAttribute('class', 'justify-content-between');
                itemDiv.appendChild(nameSpan);
                nameSpan.innerHTML = route.name;
            });
        }
    })
}