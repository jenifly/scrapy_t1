CREATE DATABASE `jenifly_music` DEFAULT CHARACTER SET utf8;

USE jenifly_music;

CREATE TABLE _music (
	_index int unsigned NOT NULL AUTO_INCREMENT,
	_id int unsigned NOT NULl,
	_name varchar(64) NOT NULL,
	_rank int unsigned NOT NULL,
	_singer varchar(32) NOT NULL,
	_duration varchar(12) NOT NULL,
	_album varchar(32) NOT NULL,
	_pic_url varchar(64) NOT NULL,
	_lrc_url varchar(64) NOT NULL,
	_song_url varchar(64) NOT NULL,
	_belong int unsigned NOT NULL,
	_updatetime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	_createtime datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY (_index),
	UNIQUE (_belong)
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;