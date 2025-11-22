const http = require('http');
const hostname = '192.168.56.1';
const port = 31400;
const server = http.createServer((req, res) => {
 res.statusCode = 200;
 res.setHeader('Content-Type', 'text/plain');
 res.end('Hello World');
});
server.listen(port, hostname, () => {
 console.log(`Server running at http://192.168.56.1:31400/`);
});
