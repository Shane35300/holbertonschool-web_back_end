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

describe('Cart page', () => {
    it('should return status code 200 when id is a number', (done) => {
        request.get(`${BASE_URL}/cart/12`, (error, response, body) => {
            expect(response.statusCode).to.equal(200);
            expect(body).to.equal('Payment methods for cart 12');
            done();
        });
    });

    it('should return status code 404 when id is NOT a number', (done) => {
        request.get(`${BASE_URL}/cart/hello`, (error, response, body) => {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
