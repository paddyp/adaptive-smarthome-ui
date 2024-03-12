import { Component } from '@angular/core';
import { BaseComponentComponent } from '../../base-component/base-component.component';
import { IntToHexPipe } from '../../int-to-hex.pipe';
import { CommonModule } from '@angular/common';
import { CurrentValuesComponent } from '../../current-values/current-values.component';
@Component({
  selector: 'app-button',
  standalone: true,
  imports: [IntToHexPipe, CommonModule, CurrentValuesComponent],
  templateUrl: './button.component.html',
  styleUrl: './button.component.scss'
})
export class ButtonComponent extends BaseComponentComponent {

  setMaxValue(): void {
    this.data.current_value = this.data.max;
    this.sendChangedValues(this);
  }
}
