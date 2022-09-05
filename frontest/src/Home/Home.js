import "./Home.css";

import { useState } from "react";
import Bloglist from "../Bloglist";

const Home = () => {
  const [div, setDiv] = useState([
    {
      id: 1,
      nom: "oumar Thiombane",
      commentaire:
        "Lorem ipsum dolor sit amet consectetur adipiscing elit, eget neque maecenas natoque bibendum senectus, aliquet mi ultricies quisque nisl enim. Aenean netus turpis blandit nibh tincidunt vulputate, rutrum in neque nisi condimentum ridiculus, pharetra praesent fames lobortis quis. Vel magnis dis eros ante nibh class odio, tempus integer fames euismod donec commodo auctor, volutpat fringilla justo nec dictumst per.",
      age: 24,
      sexe: "masculin",
      date_de_naissance: "25/12/1997",
    },
    {
      id: 2,
      nom: "Coumba Ndiaye",
      prenom:
        "Convallis senectus rutrum in arcu nascetur mollis eu feugiat quisque felis sed sagittis, per dui cum sapien vel tincidunt volutpat taciti nam fusce. Torquent vulputate praesent sagittis nullam gravida posuere tincidunt parturient et mattis magnis, duis nec tempus feugiat nisl cras sed pretium accumsan nisi, arcu natoque curae himenaeos nostra facilisis rutrum venenatis integer faucibus",
      age: 23,
      sexe: "Feminin",
      date_de_naissance: "02/05/1999",
    },
    {
      id: 3,
      nom: "Coumba Ndiaye",
      prenom:
        "Convallis senectus rutrum in arcu nascetur mollis eu feugiat quisque felis sed sagittis, per dui cum sapien vel tincidunt volutpat taciti nam fusce. Torquent vulputate praesent sagittis nullam gravida posuere tincidunt parturient et mattis magnis, duis nec tempus feugiat nisl cras sed pretium accumsan nisi, arcu natoque curae himenaeos nostra facilisis rutrum venenatis integer faucibus",
      age: 23,
      sexe: "Feminin",
      date_de_naissance: "02/05/1999",
    },
  ]);
  const supprimer =(id)=>{
    const newdiv= div.filter ((div)=>div.id !== id);
    setDiv(newdiv);
}

  const omzostate = () => {};
  return (
    <div className="Home">
      <Bloglist div={div} titre={"Liste des blogs"} supprimer={supprimer}/>
      {/* <Bloglist div={div.filter((di) => di.nom === "Coumba Ndiaye")} titre={"Liste des blogs de coumba ndiaye"} /> */}
    </div>
  );
};

export default Home;
