function carregar() {
    var msg = document.querySelector('#msg')
    var img = document.querySelector('#imagem')
    var data = new Date()
    hora = data.getHours()
    msg.innerHTML = `Agora são ${hora} horas.`
    if (hora >= 0 && hora < 12) {
        //BOM DIA!
        img.src = 'fotomanha.jpg'
        document.body.style.background = '#E2CD9F'
    } else if(hora > 12 && hora <= 18) {
        //BOA TARDE!
        img.src = 'fototarde.jpg'
        document.body.style.background = '#B9846F'
    } else {
        //BOA NOITE!
        img.src = 'fotonoite.jpg'
        document.body.style.background = '#515154'
    }
}