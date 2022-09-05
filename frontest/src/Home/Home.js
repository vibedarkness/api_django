import "./Home.css";

import { useState, useEffect } from "react";
import Bloglist from "../Bloglist";

const Home = () => {
  const [div, setDiv] = useState(null);
  useEffect(() => {
    fetch("http://localhost:8000/div")
      .then((response) => {
        return response.json();
      })
      .then((data) => {
        setDiv(data);
      });
  }, []);
//     const supprimer =(id)=>{
//       const newdiv= div.filter ((div)=>div.id !== id);
//       setDiv(newdiv);
//   }

//   const omzostate = () => {};
  return (
    <div className="Home">
{ div && <Bloglist div={div} titre={"Liste des blogs"} />}
      {/* <Bloglist div={div.filter((di) => di.nom === "Coumba Ndiaye")} titre={"Liste des blogs de coumba ndiaye"} /> */}
    </div>
  );
};

export default Home;
