import  React, { Component } from  'react';
import  SpellService  from  './SpellService';

const  spellService  =  new  SpellService();

class  SpellsList  extends  Component {

    constructor(props) {
        super(props);
        this.state  = {
            spells: [],
            nextPageURL:  ''
        };
        // this.nextPage  =  this.nextPage.bind(this);
    }
    componentDidMount() {
    var  self  =  this;
    spellService.getSpells().then(function (result) {
        console.log('privet')
        console.log(result);
        self.setState({ spells:  result, nextPageURL:  result.nextlink})
    });
    }
//     nextPage(){
//     var  self  =  this;
//     spellService.getSpellsByURL(this.state.nextPageURL).then((result) => {
//         self.setState({ spells:  result.data, nextPageURL:  result.nextlink})
//     });
// }
render() {

    return (
    <div  className="spells--list">
        <table  className="table">
            <thead  key="thead">
            <tr>
                <th>#</th>
                <th>Name</th>
                <th>Text</th>
                <th>Level</th>
                <th>School</th>
                <th>Casting time</th>
                <th>Components</th>
                <th>Range</th>
                <th>Materials</th>
                <th>Duration</th>
                <th>Ritual</th>
                <th>Concentration</th>
            </tr>
            </thead>
            <tbody>
                {this.state.spells.map( c  =>
                <tr  key={c.id}>
                    <td>{c.id}  </td>
                    <td>{c.name}</td>
                    <td>{c.text}</td>
                    <td>{c.level}</td>
                    <td>{c.school}</td>
                    <td>{c.casting_time}</td>
                    <td>{c.componens}</td>
                    <td>{c.range}</td>
                    <td>{c.materials}</td>
                    <td>{c.duration}</td>
                    <td>{c.ritual}</td>
                    <td>{c.concentration}</td>
                    <td>
                    </td>
                </tr>)}
            </tbody>
        </table>
        <button  className="btn btn-primary"  onClick=  {  this.nextPage  }>Next</button>
    </div>
    );
}
}
export  default  SpellsList;
