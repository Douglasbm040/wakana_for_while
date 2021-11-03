const axios = require('axios');

function url(host ,local) {
    
    url=host+local
    return url
    
}

(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:5000/service/Praia da Costa, Vila Velha - ES')
    console.log(response.data);

  } catch (error) {
    console.log(error.response.body);
  }
})();
