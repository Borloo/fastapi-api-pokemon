import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PokemonsComponent } from './pokemons/pokemons.component';
import {HttpClientModule} from "@angular/common/http";
import { PokemonComponent } from './pokemon/pokemon.component';

@NgModule({
  declarations: [
    AppComponent,
    PokemonsComponent,
    PokemonComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
