import { isString } from 'util';
import { ValidatorFn, FormGroup, ValidationErrors } from '@angular/forms';

export function isEmptyNullUndefined(variable: any): boolean {
  if(isString(variable)) return variable === '' || variable === null || variable === undefined;
  return variable === null || variable === undefined;
}

export const myPortionValidator: ValidatorFn = (control: FormGroup): ValidationErrors | null => {
  const person = control.get('person').value;
  const myPortion = control.get('myPortion').value;
  return person.name !== 'No one' && (isEmptyNullUndefined(myPortion) || Number(myPortion) > 100 || Number(myPortion) < 0) ?
    { noPortion: true } : null
}
