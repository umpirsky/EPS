<?php

require_once __DIR__.'/vendor/autoload.php';

use Goutte\Client;

$client = new Client();

for ($i=0; $i < 1000; $i++) {
    $crawler = $client->request('GET', 'http://www.jugoistok.com/prikazracuna/index.php/registracija_korisnika');
    $form = $crawler->selectButton('Registrujte se')->form();
    $crawler = $client->submit($form, [
        'ime' => 'Ivan',
        'prezime' => 'Golubovic',
        'telefon' => '1234567',
        'email' => sprintf('golub+%d@jugoistok.com', $i),
        'user_password' => 'opaaa',
        'user_password_potvrda' => 'opaaa',
        'uslovi_koriscenja' => 'da',
    ]);

    $crawler->filter('.alert')->each(function ($node) {
        echo $node->text();
    });
}
