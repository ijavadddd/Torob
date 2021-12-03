create database db_torob;

use db_torob;

create table t_verifiedSellers(
		sellerCode int primary key not null auto_increment ,
		sellerName varchar(30) not null,
		sellerSiteURL varchar(250) not null,
		sellerEnamadURL	varchar(350),
		sellerLogoAddress varchar(350),
		sellerContactInfo varchar(500),
		sellerStatus int not null ,
        sellerScriptModule text(6553)
		);
        
use db_torob;
create table t_torobProducts(
		sellerCode int not null,
		sellerName varchar(100)  not null,
        poductCode int auto_increment not null  primary key,
		productCategori varchar(35),
		productName varchar(350) not null,
		productImageURL varchar(700),
		productPrice varchar(30) not null,
        productLinkURL varchar(700) not null
		);

use db_torob;
create table t_temporaryResultSearch(
		sellerCode int not null,
		sellerName varchar(100)  not null,
        poductCode int auto_increment not null  primary key,
		productCategori varchar(35),
		productName varchar(350) not null,
		productImageURL varchar(700),
		productPrice varchar(30) not null,
        productLinkURL varchar(700) not null
		);
