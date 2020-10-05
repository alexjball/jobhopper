import defaultApi from '..';
import FakeApi from '../FakeApi';
import { Occupation } from '../../domain/occupation';
import { Transition } from '../../domain/transition';

describe('Fake API', () => {
  it('Fake can be constructed', () => {
    expect(new FakeApi()).toBeDefined();
  });

  it('is provided by default', () => {
    expect(defaultApi).toBeInstanceOf(FakeApi);
  });

  it('retrieves occupations', async () => {
    const api = new FakeApi();
    const occupations: Occupation[] = await api.getOccupations();
    occupations.forEach(({ name, code }) => {
      expect(typeof name).toBe('string');
      expect(typeof code).toBe('string');
    });
  });

  it('retrieves transitions', async () => {
    const api = new FakeApi();
    const transitions: Transition[] = await api.getTransitions();
    transitions.forEach(
      ({ name, code, annualSalary, hourlyPay, transitionRate }) => {
        expect(typeof name).toBe('string');
        expect(typeof code).toBe('string');
        expect(typeof annualSalary).toBe('number');
        expect(typeof hourlyPay).toBe('number');
        expect(typeof transitionRate).toBe('number');
      }
    );
  });
});
