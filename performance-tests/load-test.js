import http from 'k6/http';
import { check } from 'k6';

export const options = {
    vus: 10,
    duration: '10s'
};

export default function () {
    const res = http.get('https://parabank.parasoft.com/parabank/overview.htm');
    check(res, {
        'status is 500': (r) => r.status !== 500,
    });
}