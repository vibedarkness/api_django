
const Bloglist = ({div,titre,supprimer}) => {

  return (
    <div className="bloglist">

        <h2>{titre}</h2>
      {/* <div className="contenu"> */}
        {div.map((div) => (
          <div className="blog" key={div.id}>
            <a href="" className="blog-titre">
              Auteur: {div.nom}
            </a>
            <br />
            <small className="blog-pulication-date">
              Date de naissance: {div.date_de_naissance}
            </small>
            <p className="blog-author">Age: {div.age}</p>
            <button onClick={()=>supprimer(div.id)}>Supprimer Article</button>
          </div>
        ))}
      </div>
    // </div>
  );
};

export default Bloglist;
