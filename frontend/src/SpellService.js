import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class SpellService{

    getSpells() {
        const url = `${API_URL}/api/spells/`;
        return axios.get(url).then(response => response.data);
    }
    getSpellsByURL(link){
        const url = `${API_URL}${link}`;
        return axios.get(url).then(response => response.data);
    }
}