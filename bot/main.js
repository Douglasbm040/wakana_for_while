/*function get(url){
    let request = new XMLHttpRequest()
    request.open('GET',url)
    request.send()
    return request.responseText
}


function main(){
    local=prompt('adicione um local para a pesquisa :    ')
    local = 'http://127.0.0.1:5000/service/' + local
    data = get(local)
    console.log(data)
    
}
main()*/

const readline = require("readline");
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("What is your name ? ", function(name) {
    rl.question("Where do you live ? ", function(country) {
        console.log(`${name}, is a citizen of ${country}`);
        rl.close();
    });
});

rl.on("close", function() {
    console.log("\nBYE BYE !!!");
    process.exit(0);
});