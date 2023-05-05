CREATE Table client 
(
    id_client INT IDENTITY(1,1) PRIMARY KEY, 
    nom_client VARCHAR(50) NOT NULL,
    prenom_client VARCHAR(50) NOT NULL, 
    tel_client VARCHAR(40) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password_client VARCHAR(100) NOT NULL,
);


CREATE TABLE Localisation
( 
  loc_id INT IDENTITY(1,1) PRIMARY KEY,
  loc_nom VARCHAR(100) NOT NULL, 
);

CREATE TABLE voiture_category 
(
  voiture_cat VARCHAR(40) PRIMARY KEY,
  voiture_capacity INT NOT NULL,
  prix_jour FLOAT NOT NULL, 
);

CREATE TABLE voiture 
(
  matricule VARCHAR(40) PRIMARY KEY,
  v_model VARCHAR(40) NOT NULL,
  v_annee_model DATE NOT NULL, 
   voiture_cat VARCHAR(40),
    v_flag BOOLEAN NOT NULL,
    loc_id INT NOT NULL , -- Localisation
  CONSTRAINT FK_CAT  Foreign Key (voiture_cat) REFERENCES  voiture_category (voiture_cat),
  CONSTRAINT FK_loc Foreign Key (loc_id) REFERENCES Localisation(loc_id)
);

CREATE Table reservation(
    res_id INT IDENTITY(1,1) PRIMARY KEY,
    date_res DATE NOT NULL, 
    date_retour DATE not NULL,
    prix_res FLOAT NOT NULL,
    flag_res BOOLEAN NOT NULL, 
    pick_loc    INT     NOT NULL, 
    drop_loc    INT NOT NULL, 
    matricule_v VARCHAR(40) NOT NULL, 
    id_client INT NOT NULL,
    CONSTRAINT FK_PICK Foreign Key (pick_loc) REFERENCES Localisation (loc_id),
     CONSTRAINT FK_DROP Foreign Key (drop_loc) REFERENCES Localisation (loc_id),
      CONSTRAINT FK_MAT Foreign Key (matricule_v) REFERENCES voiture(matricule),
       CONSTRAINT FK_Client Foreign Key (id_client) REFERENCES client(id_client)
);

CREATE TABLE facture
(
    fact_id INT IDENTITY(1,1) PRIMARY KEY,
    fact_date DATE NOT NULL,
    fact_flag BOOLEAN NOT NULL,
    prix_total FLOAT NOT NULL,
  res_id INT NOT NULL,
 CONSTRAINT FK_res Foreign Key (res_id) REFERENCES reservation(res_id)

);