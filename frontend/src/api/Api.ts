import { Occupation } from '../domain/occupation';
import { State } from '../domain/state';
import { Transition } from '../domain/transition';

type GetTransitionRequest = { state: State; occupation: { code: string } };

export default interface Api {
  getOccupations: () => Promise<Occupation[]>;

  getTransitions: (request: GetTransitionRequest) => Promise<Transition[]>;
}
