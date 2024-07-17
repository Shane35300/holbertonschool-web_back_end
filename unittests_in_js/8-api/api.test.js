const request = require('request');
const { expect } = require('chai');
const app = require('./api');

const BASE_URL = 'http://localhost:7865';

describe('Index page', () => {
    it('should return status code 200', (done) => {
        request.get(BASE_URL, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return the correct message', (done) => {
        request.get(BASE_URL, (error, response, body) => {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });
});
