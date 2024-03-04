import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmDeviceIconComponent } from './sm-device-icon.component';

describe('SmDeviceIconComponent', () => {
  let component: SmDeviceIconComponent;
  let fixture: ComponentFixture<SmDeviceIconComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SmDeviceIconComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SmDeviceIconComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
