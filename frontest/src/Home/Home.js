import "./Home.css";

import { useState } from "react";

const Home = () => {
  const [div, setDiv] = useState([
    {
      id: 1,
      nom: "Thiombane",
      prenom: "oumar",
      age: 24,
      sexe: "masculin",
      date_de_naissance: "25/12/1997",
    },
    {
      id: 2,
      nom: "Ndiaye",
      prenom: "Coumba",
      age: 23,
      sexe: "Feminin",
      date_de_naissance: "02/05/1999",
    },
    
  ]);

  const omzostate = () => {};
  return (
    <div className="Home">
      <div className="contenu">
        {div.map((div) => (
          <div className="blog" key={div.id}>
            <a href="" className="blog-title">Prenom: {div.prenom}</a><br/>
            <a href="" className="blog-title">Nom: {div.nom}</a><br/>
            <a href="" className="blog-title">Age: {div.age}</a>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Home;
