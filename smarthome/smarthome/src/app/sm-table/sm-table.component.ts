import { Component, Input } from '@angular/core';
import { SmarthomeDevice } from '../smarthome-device';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-sm-table',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './sm-table.component.html',
  styleUrl: './sm-table.component.scss'
})
export class SmTableComponent {
  @Input() SmarthomeDevice!: SmarthomeDevice;
}
