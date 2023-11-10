import {Type} from "./type";
import {Skill} from "./skill";

export interface Pokemon{
  pokedex_id: number;
  name: string;
  size: number;
  weight: number;
  basic_stats: number;
  image: string;
  types: Type[];
  skills: Skill[];
}
