/*function get(url){
    let request = new XMLHttpRequest()
    request.open('GET',url)
    request.send()
    return request.responseText
}


function main(){
    
    //local=prompt('adicione um local para a pesquisa :    ')
    local= 'Praia da Costa, Vila Velha - ES'
    local = 'http://127.0.0.1:5000/service/' + local
    data = get(local)
    console.log(data)
    
}
main()*/

const fetch = require('node-fetch');

(async () => {
  try {
    

    const response = await fetch('http://127.0.0.1:5000/service/Praia da Costa, Vila Velha - ES')
    const json = await response

    console.log(json.responseText);
    //console.log(json.explanation);
  } catch (error) {
    console.log(error.response.body);
  }
})();