import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrentValuesComponent } from './current-values.component';

describe('CurrentValuesComponent', () => {
  let component: CurrentValuesComponent;
  let fixture: ComponentFixture<CurrentValuesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [CurrentValuesComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(CurrentValuesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
