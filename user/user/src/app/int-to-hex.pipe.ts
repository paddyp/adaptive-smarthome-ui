import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'intToHex',
  standalone: true
})
export class IntToHexPipe implements PipeTransform {

  transform(value: number, ...args: unknown[]): string {
    try {
      let hex = value.toString(16);
      return "#" + hex;
    } catch {
      return "";
    }
  }


}
