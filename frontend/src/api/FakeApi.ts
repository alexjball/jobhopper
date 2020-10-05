import { Occupation } from '../domain/occupation';
import { Transition } from '../domain/transition';
import occupations from '../ui/data/occupations';
import transitions from '../ui/data/transitionData';
import Api from './Api';

export default class FakeApi implements Api {
  getTransitions: () => Promise<Transition[]> = () =>
    Promise.resolve(transitions);

  getOccupations: () => Promise<Occupation[]> = () =>
    Promise.resolve(occupations);
}
