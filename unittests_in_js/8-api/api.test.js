const request = require('request');
const { expect } = require('chai');
const { exec } = require('child_process');
const killPort = require('kill-port');

describe('Index page', function() {
  let server;

  before(function(done) {
    killPort(7865)
      .then(() => {
        server = exec('node api.js');
        server.stdout.on('data', (data) => {
          if (data.includes('API available on localhost port 7865')) {
            done();
          }
        });
      })
      .catch((err) => done(err));
  });

  after(function(done) {
    server.kill();
    done();
  });

  const url = 'http://localhost:7865/';

  it('should return status 200', function(done) {
    request(url, function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', function(done) {
    request(url, function(error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });
});
