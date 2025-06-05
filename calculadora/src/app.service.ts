<<<<<<< HEAD
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    return 'Hello World!';
  }
}
=======
import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): string {
    console.log('log');
    console.error('error');
    console.warn('warn');
    console.debug('debug');
    console.info('info');
    return 'Hello World!';
  }
}
>>>>>>> 6c3af48 (Subiendo todos los archivos desde la nueva computadora)
