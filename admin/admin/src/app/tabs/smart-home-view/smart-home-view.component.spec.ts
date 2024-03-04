import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SmartHomeViewComponent } from './smart-home-view.component';

describe('SmartHomeViewComponent', () => {
  let component: SmartHomeViewComponent;
  let fixture: ComponentFixture<SmartHomeViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SmartHomeViewComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(SmartHomeViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
