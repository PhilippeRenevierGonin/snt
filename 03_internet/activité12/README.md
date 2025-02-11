# Activité 12 : Routage et internet

Sur une feuille, prenez note des exercices. L'activité sera peut-être ramassée. 

## Exercice 1 : routage

Il s'agit de l'exercice 4 page 50 du manuel "SNT, édition Delagrave".


## Exercice 2 : localisation des IP

[Sur la page localiser-une-adresse-ip](https://mon-adresse-ip.fr/localiser-une-adresse-ip) il est possible de trouver la localisation d'une IP dans le monde. Ce n'est pas la seule page qui rend ce service. 

Voici les entêtes d'un courriel reçu sur une adresse @univ-cotedazur.fr dont les courriels sont gérés par microsoft. La première partie concerne la réception et le traitement du couriel :

```
Received: from PAZP264MB2573.FRAP264.PROD.OUTLOOK.COM (2603:10a6:102:1e4::19)
 by PR1P264MB3958.FRAP264.PROD.OUTLOOK.COM with HTTPS; Mon, 13 Jan 2025
 09:57:01 +0000
Received: from AS4PR09CA0007.eurprd09.prod.outlook.com (2603:10a6:20b:5e0::8)
 by PAZP264MB2573.FRAP264.PROD.OUTLOOK.COM (2603:10a6:102:1e4::19) with
 Microsoft SMTP Server (version=TLS1_2,
 cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id 15.20.8335.18; Mon, 13 Jan
 2025 09:56:58 +0000
Received: from AMS1EPF0000004E.eurprd04.prod.outlook.com
 (2603:10a6:20b:5e0:cafe::48) by AS4PR09CA0007.outlook.office365.com
 (2603:10a6:20b:5e0::8) with Microsoft SMTP Server (version=TLS1_3,
 cipher=TLS_AES_256_GCM_SHA384) id 15.20.8335.18 via Frontend Transport; Mon,
 13 Jan 2025 09:56:58 +0000
Authentication-Results: spf=none (sender IP is 134.59.190.214)
 smtp.mailfrom=oldmail.sust.edu; dkim=none (message not signed)
 header.d=none;dmarc=none action=none header.from=oldmail.sust.edu;
Received-SPF: None (protection.outlook.com: oldmail.sust.edu does not
 designate permitted sender hosts)
Received: from ip-sophia01.unice.fr (134.59.190.214) by
 AMS1EPF0000004E.mail.protection.outlook.com (10.167.16.139) with Microsoft
 SMTP Server (version=TLS1_2, cipher=TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384) id
 15.20.8356.11 via Frontend Transport; Mon, 13 Jan 2025 09:56:58 +0000
```

La première partie des entêtes concerne l'émission du couriel :

```
[...]
Received: from oldmail.sust.edu ([103.84.159.10])
  by ip-sophia06.unice.fr with ESMTP/TLS/ECDHE-RSA-AES128-GCM-SHA256; 13 Jan 2025 10:56:56 +0100
Received: from localhost (localhost [127.0.0.1])
	by oldmail.sust.edu (Postfix) with ESMTP id 022934C5E8FB1;
	Sun, 12 Jan 2025 14:31:41 +0600 (+06)
Received: from oldmail.sust.edu ([127.0.0.1])
	by localhost (oldmail.sust.edu [127.0.0.1]) (amavisd-new, port 10032)
	with ESMTP id bepYFWXZXto6; Sun, 12 Jan 2025 14:31:41 +0600 (+06)
Received: from localhost (localhost [127.0.0.1])
	by oldmail.sust.edu (Postfix) with ESMTP id 452334CC5198C;
	Sat, 11 Jan 2025 15:42:57 +0600 (+06)
X-Virus-Scanned: amavisd-new at sust.edu
Received: from oldmail.sust.edu ([127.0.0.1])
	by localhost (oldmail.sust.edu [127.0.0.1]) (amavisd-new, port 10026)
	with ESMTP id UoMbLpvtQeh9; Sat, 11 Jan 2025 15:42:57 +0600 (+06)
Received: from [192.168.0.102] (unknown [102.69.221.96])
	by oldmail.sust.edu (Postfix) with ESMTPSA id A0B8E4CBF8932;
	Sat, 11 Jan 2025 13:39:43 +0600 (+06)
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Description: Mail message body
Subject: =?utf-8?q?s=C3=A9lectionn=C3=A9e_pour_recevoir_une_compensation_de_950=2C?=
 =?utf-8?q?000=2E00_=28EURO=29?=
To: monir <monir@oldmail.sust.edu>
From: monir@oldmail.sust.edu
Date: Sat, 11 Jan 2025 08:39:34 +0100
Reply-To: organizationeu@gmail.com
Message-Id: <20250111073944.A0B8E4CBF8932@oldmail.sust.edu>
Content-Transfer-Encoding: base64
Return-Path: monir@oldmail.sust.edu
```

et voici le contenu du message : 

```
European Commission
European Anti-Fraud Commission, “EAFC”
1049 Brussels
Belgium

Cher propriétaire de l’e-mail.

Votre adresse e-mail a été sélectionnée pour recevoir une compensation de 950,000.00 (EURO) de la Commission européenne de lutte antifraude.
Cette indemnisation est versée pour les pertes/dommages que vous auriez pu subir à la suite d’une expérience de fraude ou d’escroqueries.
Veuillez nous répondre avec vos informations comme indiqué ci-dessous.

Votre nom complet :
Pays:
Numéro de téléphone:
Âge:
Occupation:

Toutes les informations doivent être transmises à la Commission européenne de lutte antifraude, « EAFC » ici à cette adresse e-mail (organizationeu@gmail.com).

Unité de surveillance Département
Commission européenne de lutte antifraude (EAC)
organizationeu@gmail.com
```

Pour rappel, les adresses IP 127.0.0.1 ou 192.168.0.102 ne sont pas localisables car ce sont des adresses "locales" (soit une adresse interne à l'ordinateur soit celle d'un réseau privé). 
voici les questions : 
- 2.1 Identifiez les adresses IP disponibles dans ces entêtes et localisez-les. 
- 2.2 les ips (ipv6 ou ipv4) liées à la reception correspondent-elles à des traitement par microsoft puis l'Université Côte d'Azur (située entre autre à Nice, Sophia Antipolis, etc.)
- 2.3 d'où provient le message ? 
- 2.4 Ce courriel est-il crédible ? 

## Exercice 3 : localisation des IP entre chez moi et google

Voici une "tracert" (traceroute sous windows) fait depuis chez moi pour "google.com". Ce "tracert" permet de voir les étapes pour que depuis chez moi, je puisse atteindre google. 
```
Détermination de l’itinéraire vers google.com [2a00:1450:4007:80d::200e]
avec un maximum de 30 sauts:
  1     3 ms     3 ms     3 ms  livebox.home [2a01:cb14:3de:7a00:a87:c6ff:fe5f:1a0]
  2    10 ms     9 ms     9 ms  2a01cb08a004020c0193025300750082.ipv6.abo.wanadoo.fr [2a01:cb08:a004:20c:193:253:75:82]
  3     *        *        *     Délai d’attente de la demande dépassé.
  4     *       14 ms     *     2a01:cfc4:0:a00::9
  5    55 ms    53 ms    14 ms  2001:4860:1:1::138
  6    53 ms    16 ms    51 ms  2001:4860:0:1::8341
  7    17 ms    48 ms    15 ms  2001:4860:0:1::8334
  8    35 ms    42 ms    22 ms  2001:4860::c:4003:569a
  9    26 ms    22 ms    24 ms  2001:4860::c:4002:51c9
 10    22 ms    22 ms    21 ms  2001:4860::9:4000:e7b3
 11    22 ms    21 ms    20 ms  par10s41-in-x0e.1e100.net [2a00:1450:4007:80d::200e]``` 
```
Répondez aux questions suviantes :
 - 3.1 quel est mon fournisseur d'accès ?
 - 3.2 quand le message quitte-t-il la France ?
 - 3.3 le chemin pour atteindre la destination finale est-il le plus court "à vol d'oiseau" ? 
 - 3.4 donnez une explication possible qui explique que je n'atteigne pas directement le dernier ordinateur ? 


